// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "ItemBase.h"
#include "WeaponItem.generated.h"

/**
 * 
 */

UENUM(BlueprintType)
enum class ItemDamageType : uint8
{
	UNINITIALIZED = 0,
	PIERCING, 
	SlASHING,
	BLUDGEONING,
	FIRE,
	ICE,
	LIGHTNING,
	POISON
};

UENUM(BlueprintType)
enum class WeaponType : uint8
{
	UNINITIALIZED = 0,
	MELEE,
	RANGED,
	SPELL
};

UCLASS()
class MODULARCHARSTATS_API UWeaponItem : public UItemBase
{
	GENERATED_BODY()
public:
	UWeaponItem();

	void Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, FString _itemName, 
		CharacterItemType _itemType,CharacterItemTier _itemTier, const float _weaponDamage, const float _weaponRange, const float _armorPierce, 
		ItemDamageType _damageType, WeaponType _weaponType);

	void Attack(AActor* actor) const;

	//UI send
	float GetWeaponDamage() const;
	float GetWeaponRange() const;
	float GetWeaponPierce() const;
	ItemDamageType GetWeaponDamageType() const;
	WeaponType GetWeaponType() const;

protected:

	float weaponDamage;
	float weaponRange;
	float armorPierce;
	ItemDamageType damageType;
	WeaponType weaponType;
};
