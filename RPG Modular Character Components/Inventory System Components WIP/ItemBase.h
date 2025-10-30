// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "ItemBase.generated.h"

UENUM(BlueprintType)
enum class CharacterItemType : uint8
{
	UNINITIALIZED = 0,
	WEAPON,
	ARMOR,
	ELIXIR,
	AMMUNITION,
	FOOD,
	DRINK,
	VALUABLES,
	CURRENCY,
	MISC

};

UENUM(BlueprintType)
enum class CharacterItemTier : uint8
{
	UNINITIALIZED = 0,
	COMMON,
	UNCOMMON,
	RARE,
	EPIC,
	LEGENDARY,

};

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class MODULARCHARSTATS_API UItemBase : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UItemBase();
protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	//virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;
	float getWeight() const;
	float getCost() const;
	int GetCurrentStackSize() const;
	int GetMaxStackSize() const;
	FString GetCharacterItemName() const;
	CharacterItemTier GetCharacterItemTier() const;
	CharacterItemType GetCharacterItemType() const;

	void AdjustStackSize(const int amount);

protected:
	void Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, FString _name, CharacterItemType _type, CharacterItemTier _tier);

	int maxStackSize;
	int currentStackSize;
	float weight;
	float currencyCost;
	//UPROPERTY(EditAnywhere, BlueprintReadWrite, Category ="Item")
	FString itemName;
	CharacterItemType itemType;
	CharacterItemTier itemTier;
};
