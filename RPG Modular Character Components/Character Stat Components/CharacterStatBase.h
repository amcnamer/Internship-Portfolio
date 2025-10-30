// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "CharacterStatBase.generated.h"

UENUM(BlueprintType)
enum class CharStatName : uint8
{
	UNINITIALIZED = 0,
	HEALTH = 1,
	STAMINA = 2,
	HUNGER = 3,
	THIRST = 4
};
class UCharacterStatComponent;

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class MODULARCHARSTATS_API UCharacterStatBase : public UActorComponent
{
	GENERATED_BODY()

	friend class UCharacterStatComponent;

	//Functions
public:
	UCharacterStatBase();
	UCharacterStatBase(const float current, const float max, const float regenRate, CharStatName name);



protected:
	virtual void BeginPlay() override;

	float GetCurrent() const;
	float GetMax() const;
	float GetRegenRate() const;
	CharStatName GetName() const;

	void Set(const float current, const float max, const float regen, CharStatName name);
	void SetCurrent(const float amount);
	void SetMax(const float amount);
	void SetRegenRate(const float amount);
	void SetName(CharStatName name);
	void PassiveTick();


	//Data
private:

	float current;
	float max;
	float regenRate;
	CharStatName name;
};
