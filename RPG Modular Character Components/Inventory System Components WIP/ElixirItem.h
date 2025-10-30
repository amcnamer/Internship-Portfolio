// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "ItemBase.h"
#include "ElixirItem.generated.h"

/**
 * 
 */

UENUM(BlueprintType)
enum class ElixirType : uint8
{
	UNINITIALIZED = 0,
	HEALTH,
	STAMINA
};

UCLASS()
class MODULARCHARSTATS_API UElixirItem : public UItemBase
{
	GENERATED_BODY()

public:

	UElixirItem();
	


	void Use(AActor* actor) const;

	//UI Send
	float GetStatAdjustmentAmount() const;
	ElixirType GetElixirType() const;

	void Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, 
		const float _statAdjustmentAmount, ElixirType _elixirType, FString _name, CharacterItemType _type, CharacterItemTier _tier);

public:

	float statAdjustmentAmount;
	ElixirType elixirType;

};
